import axios from "axios";
import jsdom from "jsdom"
// import express from "express"

const characters = [
    "Anre",
    "Avatar Belial",
    "Beelzebub",
    "Belial",
    "Cagliostro",
    "Charlotta",
    "Djeeta",
    "Eustace",
    "Ferry",
    "Gran",
    "Katalina",
    "Ladiva",
    "Lancelot",
    "Lowain",
    "Metera",
    "Narmaya",
    "Percival",
    "Seox",
    "Soriz",
    "Vaseraga",
    "Vira",
    "Yuel",
    "Zeta",
    "Zooey"
]

function getFrameData(dom) {
    let cats = dom.querySelector("div.attack-info thead").textContent;
    cats = cats.split("\n");
    dom.querySelectorAll("p").forEach(x => x.remove())
    dom.querySelectorAll("span.input-badge").forEach(x => x.remove())
    const regex = new RegExp("(.*\\n){5,}");
    let frameData = [].slice.call(dom.querySelectorAll("div.attack-info tbody tr"));
    //querySelectorAll("span.input-badge").forEach(x => x.remove())
    frameData = frameData.map(x => x.textContent).filter(x => regex.test(x))
    frameData = frameData.map(x => {
        x = x.trimStart().split("\n")
        return x.slice(0, x.length - 1)
    });
    for (let val of frameData) {
        if (val.length === 9) {
            val.splice(0, 1)
        }
    }
    const relation = x => x.parentNode.parentNode.nextElementSibling.children["1"].children["0"]
    let missingMoves = Array.from(new Set([].slice.call(dom.querySelectorAll("td[class = field_Version]")).map(x => x.textContent)))
    let moveNames = [].slice.call(dom.querySelectorAll("h3 > span.mw-headline big")).filter(x => relation(x))//.map(x => x.textContent);
    let count = moveNames.map(x => relation(x)).filter(x => x).map(x => x.children["1"]).filter(y => y).map(x => x.children["length"]);
    moveNames = moveNames.map(x => x.textContent);
    let fullMoves = [];
    for (let i = 0; i < count.length; i++) {
        if (count[i] > 1)
            fullMoves.push(...missingMoves.splice(0, count[i]));
        else fullMoves.push(moveNames[i]);
    }
    frameData = frameData.map(fd => Object.fromEntries(fd.map((x, i) => [cats[i], x])))
    let moveSet = Object.fromEntries(fullMoves.map((x, i) => [x, frameData[i]]))
    return JSON.stringify(moveSet);
}



function getCharFd(name = "Gran") {
    const baseUrl = "https://dustloop.com/w/GBVS/"
    axios.get(baseUrl + name)
    .then((page) => {
        // console.log(page.data)
        const dom = new jsdom.JSDOM(page.data);
        return getFrameData(dom.window.document)
    }).then(frameData => {
        return {name:frameData}
    }).catch((err) => {
        console.log(`Something Went Wrong\n${err}`)
    })
}

// getCharFd(process.argv[2])

Promise.all(characters.map(x => getCharFd(x))).then(fds => console.log(fds))