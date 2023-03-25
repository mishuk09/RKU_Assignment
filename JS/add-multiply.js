// function calculate(chair, table, bed) {

//     const perChairwood = 3;
//     const perTablewood = 6;
//     const perBedwood = 10;

//     const c = perChairwood * chair;
//     const t = perTablewood * table;
//     const b = perBedwood * bed;

//     const tottalWood = c + t + b;
//     return tottalWood;
// }

// const result = calculate(1, 1, 1);
// console.log(result);


// for (let i = 0; i < 50; i++) {
//     if (i % 3 == 0) {

//     }
// }


const phone = [


    {
        name: 'abc',
        price: 15000,
        camera: 10,
        Stor: 16
    }, {
        name: 'xiomi',
        price: 14000,
        camera: 10,
        Stor: 16
    }, {
        name: 'samsung',
        price: 12000,
        camera: 10,
        Stor: 16
    }, {
        name: 'nokia',
        price: 16000,
        camera: 10,
        Stor: 16
    }
]

let cheapest = phone[0];
for (const i of phone) {

    if (phone.price < cheapest.price) {
        cheapest = i;
    }

}
console.log(cheapest);