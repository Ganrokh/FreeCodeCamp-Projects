function rot13(str) { // LBH QVQ VG!

    let answer = str.split('');
    for (let i = 0; i < answer.length; i++) {
  
    if (answer[i].match(/[A-Z]/)){
      if (answer[i].charCodeAt(0) + 13 > 90){
        answer[i] = String.fromCharCode(answer[i].charCodeAt(0)-13);
      } else {
        answer[i] = String.fromCharCode(answer[i].charCodeAt(0)+13);
      }
    }
    }
    return answer.join('');
  }
  
  // Change the inputs below to test
  rot13("SERR PBQR PNZC");