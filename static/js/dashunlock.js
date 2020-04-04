function getSelectedOptions(sel, fn){
    var opts = [], opt;
    for (var i =0, len = sel.options.length; i<len; i++){
        opt = sel.options[i];

        if(opt.selected){
            opts.push(opt);

            if(fn){
                fn(opt);
            }
        }
    }

    return opts;
}

function callback(opt){
    var display = document.getElementById("feature-select-div");
    display.innerHTML +=opt.value+', ';
}

document.getElementById("paramcollopt").onchange = function(e){
    var display = document.getElementById("feature-select-div");
    display.innerHTML = '';

    getSelectedOptions(this, callback);
    
    var str = display.innerHTML.slice(0,-2);
    display.innerHTML = str;
}

$("#optybtn").click(function () {
    $("#feature-select-div").show();
    
    $("#submit-btn").hide();
});



$("#optnbtn").click(function () {
    $("#submit-btn").show();
    $("#feature-select-div").hide();
    $("#more-options").hide();

});



