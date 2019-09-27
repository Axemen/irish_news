TESTER = document.getElementById('tester');
// TESTER = d3.select('tester').html;

plot = Plotly.plot( TESTER, [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16]}, 
    {
    margin: {t: 0} 
    }
]);
console.log('test');
console.log(plot)
selectMe = d3.select('selectMe');
console.log(selectMe);