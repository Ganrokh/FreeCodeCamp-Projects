function convertToRoman(num) {
    let rome = '';
    const digitNum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const romNum = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  
    for(let i = 0; i < digitNum.length; i++){
      while(num >= digitNum[i]){
        num -= digitNum[i];
        rome += romNum[i];
      }
    }
  
  
   return rome;
  }
  
  convertToRoman(36);