function getSelectedOptions(sel) {
    var opts = [], opt;
    for (var i = 0, len = sel.options.length; i < len; i++) {
        opt = sel.options[i];

        if (opt.selected) {
            opts.push(opt);

            /**if(fn){
                fn(opt);
            }*/
        }
    }

    return opts;
}


function createSelect(option_list, select) {
    var option;
    for (var i = 0; i < option_list.length; i++) {
        option = document.createElement('option');
        option.value = option_list[i];
        option.text = option_list[i];
        select.appendChild(option);
    }
}



$("#database").change(function () {
    var selectedDB = $(this).children("option:selected").val();
    console.log(selectedDB);
    if (selectedDB == "mimic") {
        $("#opts-mimic").show();
        $("#opts-eicu").hide();
    }
    else {
        $("#opts-mimic").hide();
        $("#opts-eicu").show();
    }
});




$("#optybtn").click(function () {
    $("#feature-select-div").show();
    //$("#opts").children.prop('disabled', true);
    $("#submit-btn").hide();
});



$("#optnbtn").click(function () {
    $("#submit-btn").show();
    $("#feature-select-div").hide();
    $("#more-options").hide();

});

