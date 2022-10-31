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
    console.log(Object.keys(moveSet));
    document.querySelector("body").style.display = "none";
    document.querySelector("body").append(`${Object.entries(moveSet)}`)
    return moveset;
}

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

// // x = [].slice.call(document.querySelectorAll("div.div-col dl a[title^=GBVS] > b")) #GET ALL CHARACTERS FROM https://dustloop.com/w/Granblue_Fantasy_Versus
// // x.map(z => z.innerText).sort((x,y) => x >= y)

let char_sels = document.querySelectorAll("form");
for (let sel of char_sels) {
    let form = sel.elements.characters
    for (let char of characters) {
        let option = document.createElement("option");
        option.value = char
        option.innerText = char
        form.appendChild(option)
    }
}
char_sels[0].elements.characters.value = "Gran"
char_sels[1].elements.characters.value = "Djeeta"

char_sels.forEach(sel => sel.addEventListener("change", e => {
    let img = sel.querySelector("img")
    let character = sel.elements.characters.value;
    img.src = `sprites/${character}_portrait.png`
    img.alt = `${character} Sprite`
}))
