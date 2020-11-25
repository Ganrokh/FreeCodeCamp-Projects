function palindrome(str) {
    const first = str.replace(/[^0-9a-z]/gi, '').toLowerCase();
    const second = first.split('').reverse().join('');
  
    return first === second;
  }
  palindrome("eye");