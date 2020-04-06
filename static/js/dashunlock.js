function getSelectedOptions(sel){
    var opts = [], opt;
    for (var i =0, len = sel.options.length; i<len; i++){
        opt = sel.options[i];

        if(opt.selected){
            opts.push(opt);

            /**if(fn){
                fn(opt);
            }*/
        }
    }

    return opts;
}


function createSelect(option_list, select){
    var option;
    for (var i =0; i<option_list.length; i++){
        option = document.createElement('option');
        option.value = option_list[i];
        option.text = option_list[i];
        select.appendChild(option);
    }
}


document.getElementById("paramcollopt").onchange = function(e){
    var display = document.getElementById("feature-select-div");
    display.innerHTML = "";
    
    var labs_options = ['HCO3', 'FiO2', 'pH', 'AST', 'etc'];
    var vitals_options = ['HR', 'O2Sat', 'Temp', 'SBP'];
    var temp_list = [labs_options,vitals_options];
    
    options = getSelectedOptions(this);
    
    for (var i=0; i <options.length;i++){

        display.innerHTML += '<h4> Test '+ options[i].text + ' element </h4>';

        var sel = document.createElement('select');
        sel.multiple = true;
   
        //var option;
        if(i==0){
            createSelect(labs_options, sel);
        }
        else{
            createSelect(vitals_options, sel);
        }
        display.appendChild(sel);
        display.innerHTML +="<br/>";
        
    }
    
    
    //var str = display.innerHTML.slice(0,-2);
    //display.innerHTML = str;
}







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



