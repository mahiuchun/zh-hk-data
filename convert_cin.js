#!/usr/bin/env node

if (process.argv.length < 3) {
  console.log('Usage: node '+process.argv[1]+' table_name')
  process.exit(1);
}

var name = process.argv[2];
var fs = require('fs');
var options = {'encoding': 'utf8'};

fs.readFile(name + '.cin', options, function (err, data) {
  if (err) throw err;
  lines = data.split('\n');
  var inside = false;
  var tbl = {}
  var inv = {}
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    var len = line.length;
    for (var j = 0; j < line.length; j++) {
      if (line[j] === '#') {
        len = j;
        break;
      }
    }
    line = line.substring(0, len);
    line = line.trim();
    if (line.length === 0) {
      continue;
    }
    if (line === '%chardef begin') {
      inside = true;
    } else if (line === '%chardef end') {
      inside = false;
    } else if (!inside) {
      continue;
    } else {
      var parts = line.split(/\s+/);
      if (!(parts[0] in tbl)) {
        tbl[parts[0]] = [];
      }
      tbl[parts[0]].push(parts[1]);
      if (!(parts[1] in inv)) {
        inv[parts[1]] = [];
      }
      inv[parts[1]].push(parts[0]);
    }
  }
  fs.writeFileSync(name + '.json', JSON.stringify(tbl));
  fs.writeFileSync(name + '_inv.json', JSON.stringify(inv));
});
