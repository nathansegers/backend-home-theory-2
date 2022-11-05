const path = require('path');
const shell = require('shelljs');
const rimraf = require('rimraf');


// https://github.com/shelljs/shelljs/issues/469
process.env.PATH += (path.delimiter + path.join(process.cwd(), 'nodejs', 'node_modules', '.bin'));
process.env.PATH += (path.delimiter + path.join(process.cwd(), 'nodejs', 'node_modules'));



const PROTO_DIR = path.join('protos');
const MODEL_DIR = path.join('nodejs', 'src', 'models');
const PROTOC_PATH = path.join('nodejs', 'node_modules', 'grpc-tools', 'bin', 'protoc');
const PLUGIN_PATH = path.join('nodejs', 'node_modules', '.bin', 'protoc-gen-ts_proto');

rimraf.sync(`${MODEL_DIR}/*`, {
  glob: { ignore: `${MODEL_DIR}/tsconfig.json` },
});

const protoConfigTs = [
  `--plugin=${PLUGIN_PATH}`,

  // https://github.com/stephenh/ts-proto/blob/main/README.markdown
  "--ts_proto_opt=outputServices=grpc-js,env=node,useOptionals=messages,exportCommonSymbols=false,esModuleInterop=true",

  `--ts_proto_out=${MODEL_DIR}`,
  `--proto_path ${PROTO_DIR} ${PROTO_DIR}/*.proto`,
];

shell.exec(`${PROTOC_PATH} ${protoConfigTs.join(" ")}`, console.log);
console.log("Finished generating stubs for NodeJS")
