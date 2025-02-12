
function List(){
    const fruits = ['apple', 'banana', 'orange', 'coconut', 'pineapple'];

    const listItems = fruits.map(fruit => <li>{fruit}</li>);

    return(listItems);
}

export default List