import 'source-map-support/register';
import { credentials, ServiceError } from '@grpc/grpc-js';

import { AdditionClient, AddRequest, NumberMessage } from './models/addition';

const client = new AdditionClient('localhost:9090', credentials.createInsecure(), {
  'grpc.keepalive_time_ms': 120000,
  'grpc.http2.min_time_between_pings_ms': 120000,
  'grpc.keepalive_timeout_ms': 20000,
  'grpc.http2.max_pings_without_data': 0,
  'grpc.keepalive_permit_without_calls': 1,
});



import { createInterface } from 'readline';
import { logger } from './utils';

let argv = 'addition';
let a = 0;
let b = 0;
if (process.argv.length >= 3) {
  let _a, _b;
  [, , argv, _a, _b] = process.argv;
  if (_a) a = parseInt(_a);
  if (_b) b = parseInt(_b);
}

function addExample(a: number, b: number): void {
  /**
   * rpc add2Numbers
   */
  const param: AddRequest = {
    a: a,
    b: b,
  };
  client.add2Numbers(param, (err: ServiceError | null, res: NumberMessage) => {
    if (err) {
      return logger.error('add2Numbers err:', err.message);
    }
    logger.info('add2Numbers:', res.val);
  });
}

function addStreamExample(): void {
  /**
   * rpc addNumbersStreamRequest
   */
  const streamRequest = client.addNumbersStreamRequest((err: ServiceError | null, res: NumberMessage) => {
    if (err) {
      return logger.error('addNumbersStreamRequest:', err);
    }

    logger.info('addNumbersStreamRequest:', res.val);
    process.exit();
  });

    
  const readLine = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
  });


  readLine.setPrompt("number to add:");

  readLine
    .on('line', (line) => {
      if (line) {
        // console.log(`Line: '${line}'`);
        streamRequest.write({
          val: parseInt(line),
        });
        readLine.prompt();
      } else readLine.emit('end');
    })
    .on('end', () => {
      console.log('Done.');
      streamRequest.end();
    });

  readLine.prompt();
}

function getStreamExample(): void {
  /**
   * rpc sayFibStreamResponse
   */
  const param: AddRequest = {
    a,
    b,
  };

  const streamResponse = client.sayFibStreamResponse(param);

  streamResponse
    .on('data', (res: NumberMessage) => {
      logger.info('sayFibStreamResponse', res.val);
    })
    .on('end', () => {
      logger.info('sayFibStreamResponse done');
    })
    .on('error', (err: Error) => {
      logger.error('sayFibStreamResponse:', err);
    });
}

(async (): Promise<void> => {
  try {
    if (argv === 'stdin') {
      addStreamExample();
      return;
    } else if (argv === 'fib') {
      getStreamExample();
      return;
    } else if (argv === 'add') {
      addExample(a, b);
      return;
    } else {
      logger.info('use stdin / fib x1 x2 / add x1 x2');
    }
  } catch (err) {
    logger.error(err);
  }
})();
