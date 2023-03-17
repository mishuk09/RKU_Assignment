// var arr = [1, 2, 3, 1234, 4, 5, 6, 7, 8];
// var max = arr[0];

// for (let i = 1; i < arr.length; i++) {

//     const ele = arr[i];
//     if (max < ele) {
//         max = ele;
//     }
// }

// console.log(max);



function array(arr) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        if (result.indexOf(arr) == -1) {
            result.push(arr);
            console.log(arr[i]);
        }


    }


}


var arr = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9];
array(arr);