function changeProduct(rowId){
    let rowNodes = $(rowId)[0].children;

    const chossenProduct = products.find(product => product.id == rowNodes[0].children[0].value);

    rowNodes[2].children[0].value = chossenProduct['current_price'];

    if ($('#transactionType')[0].value == 'sales') {
        rowNodes[1].children[0].max = chossenProduct['qty'];
    }

    rowNodes[3].children[0].children[0].value = chossenProduct['current_price'] * rowNodes[1].children[0].value;
    calculateGrandTotal();
}

function changeAmount(rowId) {
    let rowNodes = $(rowId)[0].children;

    rowNodes[3].children[0].children[0].value = rowNodes[1].children[0].value * rowNodes[2].children[0].value;
    calculateGrandTotal();
}

function calculateGrandTotal() {
    const rowNodes = $('.total-amount');
    let grandTotal = 0;
    for (let i = 0; i < rowNodes.length; i++) {
        grandTotal += parseInt(rowNodes[i].value);
    }
    $('#grandTotal').val(grandTotal)
    
}

function addItem() {
    $.ajax({
        url: "/admin/invoice/add-item/",
        type: "GET",
        success: function(resp){
            $("#invoice-body").append(resp);
            calculateGrandTotal();
        }
    });
}

function removeItem(rowId) {
    $(rowId).remove();
    calculateGrandTotal();
}