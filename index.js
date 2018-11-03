/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var count = 0;
    var arg = x.toString();
    
     for(var i = 0; i < Math.floor(arg.length / 2);i++) {
       if(arg.charAt(i) === arg.charAt(arg.length - i - 1)) {
           count++;
       }
     }
      
    if(count === Math.floor(arg.length / 2)) {
      return true
    }
    
    return false;
  };

console.log(isPalindrome(121));
