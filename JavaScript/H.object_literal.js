// 좌표평면의 점을 표현하는 객체
var p = {x : 1.0, y : 2.5};

// 원을 표현하는 객체
var circle = {
    center : {x : 1.0, y : 2.0},
    radius : 2.5  
};

// 회원 정보를 표현하는 객체
var person = {
    name : "kimJungmin",
    age  : 20,
    sex  : "mail",
    marry : false
};

// 프로퍼티에 저장된 값의 타입이 중요하다. 만약 타입이 '함수'라면 해당 프로퍼티를 메서드라고 부른다.
console.log(person.name);


