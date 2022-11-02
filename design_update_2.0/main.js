let moveSets = {
    "Gran": {
        "c.L": {
            "Damage": "400",
            "Guard": "Mid",
            "Startup": "5",
            "Active": "3",
            "Recovery": "6",
            "On-Block": "+2",
            "On-Hit": "+6",
            "Invuln": ""
        },
        "c.M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "6",
            "Active": "3",
            "Recovery": "12",
            "On-Block": "0",
            "On-Hit": "+4",
            "Invuln": ""
        },
        "c.H": {
            "Damage": "1200",
            "Guard": "Mid",
            "Startup": "8",
            "Active": "4",
            "Recovery": "18",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "c.XX": {
            "Damage": "350",
            "Guard": "Mid",
            "Startup": "9",
            "Active": "3",
            "Recovery": "15",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "c.XXX": {
            "Damage": "350",
            "Guard": "Mid",
            "Startup": "12",
            "Active": "4",
            "Recovery": "17",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "f.L": {
            "Damage": "400",
            "Guard": "Mid",
            "Startup": "6",
            "Active": "3",
            "Recovery": "13",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "f.M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "8",
            "Active": "3",
            "Recovery": "18",
            "On-Block": "-6",
            "On-Hit": "-2",
            "Invuln": ""
        },
        "f.H": {
            "Damage": "1000",
            "Guard": "Mid",
            "Startup": "10",
            "Active": "5",
            "Recovery": "21",
            "On-Block": "-9",
            "On-Hit": "-5",
            "Invuln": ""
        },
        "2L": {
            "Damage": "400",
            "Guard": "Low",
            "Startup": "6",
            "Active": "3",
            "Recovery": "6",
            "On-Block": "+2",
            "On-Hit": "+6",
            "Invuln": ""
        },
        "2M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "7",
            "Active": "5",
            "Recovery": "9",
            "On-Block": "+1",
            "On-Hit": "+5",
            "Invuln": ""
        },
        "2H": {
            "Damage": "1000",
            "Guard": "Mid",
            "Startup": "10",
            "Active": "6",
            "Recovery": "24",
            "On-Block": "-13",
            "On-Hit": "-9",
            "Invuln": ""
        },
        "2U": {
            "Damage": "700",
            "Guard": "Low",
            "Startup": "7",
            "Active": "6",
            "Recovery": "21",
            "On-Block": "-12",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "j.L": {
            "Damage": "400",
            "Guard": "High/Air",
            "Startup": "5",
            "Active": "Until landing",
            "Recovery": "0",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.M": {
            "Damage": "550",
            "Guard": "High/Air",
            "Startup": "6",
            "Active": "7",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.H": {
            "Damage": "800",
            "Guard": "High/Air",
            "Startup": "7",
            "Active": "6",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.U": {
            "Damage": "700",
            "Guard": "High/Air",
            "Startup": "12",
            "Active": "8",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "5U": {
            "Damage": "1000/1200/1400/1600/2000",
            "Guard": "Mid",
            "Startup": "22/20",
            "Active": "9",
            "Recovery": "13",
            "On-Block": "-5",
            "On-Hit": "",
            "Invuln": ""
        },
        "5[U] > X": {
            "Damage": "",
            "Guard": "",
            "Startup": "",
            "Active": "",
            "Recovery": "15",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "Ground Throw": {
            "Damage": "1500",
            "Guard": "Throw",
            "Startup": "7",
            "Active": "3",
            "Recovery": "31",
            "On-Block": "",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "Air Throw": {
            "Damage": "1500",
            "Guard": "Throw",
            "Startup": "5",
            "Active": "5",
            "Recovery": "Until landing +6",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "Overhead Attack": {
            "Damage": "1000",
            "Guard": "High",
            "Startup": "26",
            "Active": "6",
            "Recovery": "17",
            "On-Block": "-4",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "236L": {
            "Damage": "800",
            "Guard": "All",
            "Startup": "15",
            "Active": "",
            "Recovery": "Total 46",
            "On-Block": "-7",
            "On-Hit": "-3",
            "Invuln": ""
        },
        "236M": {
            "Damage": "400, 800",
            "Guard": "Mid, All",
            "Startup": "13",
            "Active": "4",
            "Recovery": "Total 55",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "236H": {
            "Damage": "350×3",
            "Guard": "All",
            "Startup": "15",
            "Active": "",
            "Recovery": "Total 46",
            "On-Block": "+3",
            "On-Hit": "+7",
            "Invuln": ""
        },
        "623L": {
            "Damage": "700, 300",
            "Guard": "Mid, All",
            "Startup": "9",
            "Active": "2,9",
            "Recovery": "30",
            "On-Block": "-22",
            "On-Hit": "KD",
            "Invuln": "1~10 All"
        },
        "623M": {
            "Damage": "700, 300×2",
            "Guard": "Mid×2, All",
            "Startup": "9",
            "Active": "2(3)2,17",
            "Recovery": "32",
            "On-Block": "-30",
            "On-Hit": "KD",
            "Invuln": "1~17 All"
        },
        "623H": {
            "Damage": "950~1400",
            "Guard": "Mid×3, All",
            "Startup": "9",
            "Active": "2,3,6(23)2(3)2,2,3,3,9",
            "Recovery": "32",
            "On-Block": "-30",
            "On-Hit": "HKD",
            "Invuln": "1~19 All"
        },
        "214L": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "13",
            "Active": "3",
            "Recovery": "18",
            "On-Block": "-6",
            "On-Hit": "-2",
            "Invuln": ""
        },
        "214L > 214M": {
            "Damage": "500",
            "Guard": "Mid",
            "Startup": "13",
            "Active": "13",
            "Recovery": "12",
            "On-Block": "-10",
            "On-Hit": "KD",
            "Invuln": ""
        },
        "214M": {
            "Damage": "1200",
            "Guard": "Mid",
            "Startup": "16",
            "Active": "13",
            "Recovery": "14",
            "On-Block": "+2 to -10",
            "On-Hit": "+10 to -2",
            "Invuln": ""
        },
        "214H": {
            "Damage": "1200",
            "Guard": "Mid",
            "Startup": "13",
            "Active": "13",
            "Recovery": "12",
            "On-Block": "+4 to -8",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "Tempest Blade": {
            "Damage": "3500→2500",
            "Guard": "Mid",
            "Startup": "6+5",
            "Active": "3(4)9",
            "Recovery": "23",
            "On-Block": "-13",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "Catastrophe": {
            "Damage": "4500→3500",
            "Guard": "All",
            "Startup": "8+5",
            "Active": "",
            "Recovery": "Total 98",
            "On-Block": "-18",
            "On-Hit": "HKD",
            "Invuln": ""
        }
    }, "Djeeta": {
        "c.L": {
            "Damage": "400",
            "Guard": "Mid",
            "Startup": "5",
            "Active": "3",
            "Recovery": "6",
            "On-Block": "+2",
            "On-Hit": "+6",
            "Invuln": ""
        },
        "c.M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "6",
            "Active": "3",
            "Recovery": "12",
            "On-Block": "0",
            "On-Hit": "+4",
            "Invuln": ""
        },
        "c.H": {
            "Damage": "1200",
            "Guard": "Mid",
            "Startup": "8",
            "Active": "4",
            "Recovery": "18",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "c.XX": {
            "Damage": "350",
            "Guard": "Mid",
            "Startup": "9",
            "Active": "3",
            "Recovery": "15",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "c.XXX": {
            "Damage": "350",
            "Guard": "Mid",
            "Startup": "12",
            "Active": "3",
            "Recovery": "18",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "f.L": {
            "Damage": "400",
            "Guard": "Mid",
            "Startup": "6",
            "Active": "5",
            "Recovery": "11",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "f.M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "8",
            "Active": "3",
            "Recovery": "18",
            "On-Block": "-6",
            "On-Hit": "-2",
            "Invuln": ""
        },
        "f.H": {
            "Damage": "1000",
            "Guard": "Mid",
            "Startup": "10",
            "Active": "5",
            "Recovery": "21",
            "On-Block": "-9",
            "On-Hit": "-5",
            "Invuln": ""
        },
        "2L": {
            "Damage": "400",
            "Guard": "Low",
            "Startup": "6",
            "Active": "3",
            "Recovery": "6",
            "On-Block": "+2",
            "On-Hit": "+6",
            "Invuln": ""
        },
        "2M": {
            "Damage": "700",
            "Guard": "Mid",
            "Startup": "7",
            "Active": "6",
            "Recovery": "12",
            "On-Block": "-3",
            "On-Hit": "+1",
            "Invuln": ""
        },
        "2H": {
            "Damage": "1000",
            "Guard": "Mid",
            "Startup": "10",
            "Active": "6",
            "Recovery": "24",
            "On-Block": "-13",
            "On-Hit": "-9",
            "Invuln": ""
        },
        "2U": {
            "Damage": "700",
            "Guard": "Low",
            "Startup": "7",
            "Active": "6",
            "Recovery": "21",
            "On-Block": "-12",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "j.L": {
            "Damage": "400",
            "Guard": "High/Air",
            "Startup": "5",
            "Active": "Until landing",
            "Recovery": "0",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.M": {
            "Damage": "550",
            "Guard": "High/Air",
            "Startup": "6",
            "Active": "6",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.H": {
            "Damage": "800",
            "Guard": "High/Air",
            "Startup": "7",
            "Active": "6",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "j.U": {
            "Damage": "700",
            "Guard": "High/Air",
            "Startup": "12",
            "Active": "8",
            "Recovery": "Until landing",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "5U": {
            "Damage": "800/1000/1200/1400/1800",
            "Guard": "All",
            "Startup": "28/16*",
            "Active": "5",
            "Recovery": "14",
            "On-Block": "-2",
            "On-Hit": "+3 [Forced Crouch]",
            "Invuln": "4~20 (lvl 4)"
        },
        "5[U] ~ X": {
            "Damage": "",
            "Guard": "",
            "Startup": "",
            "Active": "",
            "Recovery": "Total 15",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "Ground Throw": {
            "Damage": "1500",
            "Guard": "Throw",
            "Startup": "7",
            "Active": "3",
            "Recovery": "31",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "Air Throw": {
            "Damage": "1500",
            "Guard": "Throw",
            "Startup": "5",
            "Active": "5",
            "Recovery": "Until landing +6",
            "On-Block": "",
            "On-Hit": "",
            "Invuln": ""
        },
        "Overhead Attack": {
            "Damage": "1000",
            "Guard": "High",
            "Startup": "26",
            "Active": "6",
            "Recovery": "17",
            "On-Block": "-4 to +1",
            "On-Hit": "+1 to +6",
            "Invuln": ""
        },
        "236L": {
            "Damage": "700 (easy)\n800 (technical)",
            "Guard": "All",
            "Startup": "16",
            "Active": "",
            "Recovery": "Total 47",
            "On-Block": "-7",
            "On-Hit": "-3",
            "Invuln": ""
        },
        "236M": {
            "Damage": "700 (easy)\n800 (technical)",
            "Guard": "All",
            "Startup": "16",
            "Active": "",
            "Recovery": "Total 47",
            "On-Block": "-7",
            "On-Hit": "-3",
            "Invuln": ""
        },
        "236H": {
            "Damage": "300×3 (easy)\n300×2, 400 (technical)",
            "Guard": "All",
            "Startup": "16",
            "Active": "",
            "Recovery": "Total 47",
            "On-Block": "+2",
            "On-Hit": "+6",
            "Invuln": ""
        },
        "236[L]": {
            "Damage": "800 (easy)\n900 (technical)",
            "Guard": "All",
            "Startup": "41",
            "Active": "",
            "Recovery": "Total 69",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "236[M]": {
            "Damage": "800 (easy)\n900 (technical)",
            "Guard": "All",
            "Startup": "41",
            "Active": "",
            "Recovery": "Total 69",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "236[H]": {
            "Damage": "300×2, 400 (easy)\n300×2, 500 (technical)",
            "Guard": "All",
            "Startup": "30",
            "Active": "",
            "Recovery": "Total 60",
            "On-Block": "+8",
            "On-Hit": "+12",
            "Invuln": ""
        },
        "623L": {
            "Damage": "600, 200 (easy)\n700, 300 (technical)",
            "Guard": "Mid, All",
            "Startup": "9",
            "Active": "2,9",
            "Recovery": "30",
            "On-Block": "-14 to -22",
            "On-Hit": "+24 KD",
            "Invuln": "1~10 All"
        },
        "623M": {
            "Damage": "600, 250×2 (easy)\n700, 300×2 (technical)",
            "Guard": "Mid, All*2",
            "Startup": "12",
            "Active": "2,3,17",
            "Recovery": "29",
            "On-Block": "-22 to -27",
            "On-Hit": "+21 KD",
            "Invuln": "1~15 All"
        },
        "623H": {
            "Damage": "1200 (easy)\n1400 (technical)",
            "Guard": "Mid*3, All",
            "Startup": "9",
            "Active": "",
            "Recovery": "",
            "On-Block": "-62",
            "On-Hit": "+52 HKD",
            "Invuln": "1~19 All"
        },
        "214L": {
            "Damage": "350×2",
            "Guard": "Mid",
            "Startup": "14",
            "Active": "3(11)3",
            "Recovery": "20",
            "On-Block": "-6",
            "On-Hit": "-2",
            "Invuln": ""
        },
        "214M": {
            "Damage": "400×2",
            "Guard": "Mid",
            "Startup": "20",
            "Active": "3(13)3",
            "Recovery": "18",
            "On-Block": "-4",
            "On-Hit": "0",
            "Invuln": ""
        },
        "214X > 214X": {
            "Damage": "500",
            "Guard": "Mid",
            "Startup": "20",
            "Active": "3",
            "Recovery": "22",
            "On-Block": "-8",
            "On-Hit": "KD",
            "Invuln": ""
        },
        "214H": {
            "Damage": "300×2",
            "Guard": "Mid",
            "Startup": "15",
            "Active": "2(8)5",
            "Recovery": "18",
            "On-Block": "-6",
            "On-Hit": "-2",
            "Invuln": ""
        },
        "214H > 214H": {
            "Damage": "350×2",
            "Guard": "Mid",
            "Startup": "11",
            "Active": "2(10)3",
            "Recovery": "20",
            "On-Block": "-6",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "214H > 214H > 214H": {
            "Damage": "400",
            "Guard": "Mid",
            "Startup": "17",
            "Active": "3",
            "Recovery": "22",
            "On-Block": "-8",
            "On-Hit": "HKD",
            "Invuln": ""
        },
        "Eternal Ascendancy": {
            "Damage": "3700→2500",
            "Guard": "Mid*1, All",
            "Startup": "7+6",
            "Active": "",
            "Recovery": "",
            "On-Block": "-20, -10, -10, -10, -10, -10, -10, -10, -11, -11, -48",
            "On-Hit": "HKD",
            "Invuln": "1-17 All"
        },
        "Skyfall": {
            "Damage": "4500→3500",
            "Guard": "Mid",
            "Startup": "7+5",
            "Active": "",
            "Recovery": "",
            "On-Block": "-46 to -52",
            "On-Hit": "HKD",
            "Invuln": "1-21 All"
        }
    }
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
    // console.log(Object.keys(moveSet));
    // document.querySelector("body").style.display = "none";
    // document.querySelector("body").append(`${Object.entries(moveSet)}`)
    return moveSet;
}

function addMoves(e, char_sels) {
    let character = char_sels.elements.characters.value
    let moves = char_sels.querySelector("select[name=moves]")
    if (e.type !== "DOMContentLoaded") {
        console.log(moves.children)
        for (let move in moves.children) {
            console.log(move)
            moves.removeChild(move)
        }
    }
    for (let move in moveSets[character]) {
        let option = document.createElement("option")
        option.value = move
        option.innerText = move
        moves.appendChild(option)
    }
}



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
document.addEventListener("DOMContentLoaded", e => {
    console.log(e)
    char_sels.forEach(sel => addMoves(e, sel))
})


char_sels.forEach(sel => sel.addEventListener("change", e => {
    let img = sel.querySelector("img")
    let character = sel.elements.characters.value;
    img.src = `sprites/${character}_portrait.png`
    img.alt = `${character} Sprite`
}))


function hideInstructions () {
        // e.preventDefault()
        let results = document.querySelector("#results")
        let tableP = document.querySelector("#what_punishes")
        let instrucP = document.querySelector("#instructions > p")
        let instruc = document.querySelector("#instructions ul")
        results.classList.toggle("hidden")
        tableP.classList.toggle("hidden")
        instrucP.classList.toggle("hidden")
        instruc.classList.toggle("hidden")
        
        submit.value === "Compare" ? submit.value = "Reset" : submit.value = "Compare"
        submit.addEventListener('click', hideResults)
}

// char_sels[0].addEventListener("change", e => addMoves(e, char_sels[0]))

let submit = document.querySelector("#compare")
submit.addEventListener("click", hideInstructions, {once:true})

function hideResults () {
    document.querySelector("#instructions").classList.toggle("hidden")
    submit.value === "Compare" ? submit.value = "Reset" : submit.value = "Compare"
}

