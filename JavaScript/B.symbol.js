// create Symbol
var sym1 = Symbol();
var sym2 = Symbol();
var sym3 = Symbol("운명의 데스티니");
    
// The two values are unique to each other
console.log(sym1 == sym2);
console.log(sym3.toString());

// templet literal
var talk = `i need you, 
 tell me`;

// 보간 표현식
console.log(`to.Letter ${talk}`);

