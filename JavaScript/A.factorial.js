function factor(n) {
    if (n<=1) return n;
    return n*factor(n-1);
}

for(var i=1; i<10; i++) {
//    console.log(i + "! = " + factor(i));
    document.write(i + "! = " + factor(i) + "<br />");
}
