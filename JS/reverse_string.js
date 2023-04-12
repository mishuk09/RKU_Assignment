const name = "Hello how are you"



function reverse(text) {

    let reverse1 = '';
    for (const i of text) {

        reverse1 = i + reverse1;
        return reverse1;

    }
}
const result = reverse(name);
console.log(result);