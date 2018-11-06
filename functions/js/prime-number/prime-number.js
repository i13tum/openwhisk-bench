function getNthPrimeNumber(n){
  var count = 0;
  var num = 2;
  while(count++ != n){
    num = getNextPrimeNumber(num);
  }
  return num;
}

function getNextPrimeNumber(n){
  for(var i = ++n; i< n*n; i++){
    if(isPrime(i)) return i
  }
  return 0;
}

function isPrime(n){
  for(var i = 2; i< n; i++)
    if (n%i===0) 
      return false;
  return true;
}

function main(params) {
    var num = params.num;
    if (!num) {
    	return {
    		error: 'The input number must be specified'
    	};
    }
    var result = getNthPrimeNumber(num);
    return {
    	result: result
    };
}