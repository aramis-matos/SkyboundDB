regex = new RegExp("(.+\\t){4,}");
let frameData = [].slice.call(document.querySelectorAll("div.attack-info tbody tr"));
frameData = frameData.map(x => x.innerText);
frameData = frameData.filter(x => regex.test(x));
frameData = frameData.map(x => x.split("\t"));
temp = []
extraMoves = frameData.filter(x => x.length === 9).map(x => {temp.push(x.shift()); return x})
extraMoves = temp
let moveName = [].slice.call(document.querySelectorAll("h3 > span.mw-headline big"));
moveName = moveName.map(x => x.innerText);
for (let i = 0; i < frameData.length; i++) {

}



console.log(moveName)
console.log(frameData)
console.log(extraMoves)