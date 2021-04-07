function changeProduct(rowId){
    let rowNodes = $(rowId)[0].children;

    const chossenProduct = products.find(product => product.id == rowNodes[1].children[0].value);

    rowNodes[3].children[0].value = chossenProduct['current_price'];

    if ($('#transactionType')[0].value == 'sales') {
        rowNodes[2].children[0].max = chossenProduct['qty'];
    }

    rowNodes[4].children[0].children[0].value = chossenProduct['current_price'] * rowNodes[2].children[0].value;

}

function changeAmount(rowId) {
    let rowNodes = $(rowId)[0].children;

    rowNodes[4].children[0].children[0].value = rowNodes[2].children[0].value * rowNodes[3].children[0].value;
}

function removeItem(rowId) {
    console.log('removeItem')
}

function addItem() {
    // console.log($('#item-row-template'))
    let template = $('#item-row-template')[0].content.firstElementChild
    console.log(template)
    
    // .content.children['item-row-0']
    
    // let templateClone = (template).clone;
    // console.log(templateClone)
    // var templateChiildren =  template.children['item-row-0']
    // template.
    let template2 = template.clone
    console.log(template)
    // .appendTo("#invoice-body");
    // clone.show();
}