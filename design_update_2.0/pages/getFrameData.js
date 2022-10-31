function getFrameData() {
    let cats = document.querySelector("div.attack-info thead").innerText;
    cats = cats.replace("\n", "").split("\t");
    const stats = [].slice.call(document.querySelector("div.attack-info"));
    document.querySelectorAll("p").forEach(x => x.remove())
    regex = new RegExp("(.+\\t){4,}");
    let frameData = [].slice.call(document.querySelectorAll("div.attack-info tbody tr"));
    frameData = frameData.map(x => x.innerText).filter(x => regex.test(x)).map(x => x.split("\t"));
    let missingMoves = [];
    frameData.filter(x => x.length === 9).forEach(x => missingMoves.push(x.shift()));
    let moveNames = [].slice.call(document.querySelectorAll("h3 > span.mw-headline big"));
    let count = moveNames.map(x => x.parentElement.parentElement.nextElementSibling.lastElementChild.firstElementChild.lastElementChild.childElementCount);
    moveNames = moveNames.map(x => x.innerText);
    fullMoves = [];

    for (let i = 0; i < count.length; i++) {
        if (count[i] > 1)
            fullMoves.push(...missingMoves.splice(0, count[i]));
        else fullMoves.push(moveNames[i]);
    }
    frameData = frameData.map(fd => Object.fromEntries(fd.map((x, i) => [cats[i], x])))
    moveSet = Object.fromEntries(fullMoves.map((x, i) => [x, frameData[i]]))
    console.log(moveSet);
    // document.querySelector("body").style.display = "none";
    // document.querySelector("body").append(`${Object.entries(moveSet)}`)
    return moveSet;
}

document.addEventListener("DOMContentLoaded", getFrameData)