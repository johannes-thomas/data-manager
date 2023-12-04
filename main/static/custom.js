function toggleContract(visible) {
    var lab_contract = document.querySelector('[for="id_contract"]');
    var sel2_contract = document.querySelector('[aria-controls="select2-id_contract-container"]');
    var btns_contract = document.querySelector('[data-model-ref="contract"]');

    if (visible) {
        lab_contract.style.visibility = 'visible';
        sel2_contract.style.visibility = 'visible';
        btns_contract.style.visibility = 'visible';
    }
    else {
        lab_contract.style.visibility = 'hidden';
        sel2_contract.style.visibility = 'hidden';
        btns_contract.style.visibility = 'hidden';
    }
}

document.onreadystatechange = function () {
    if (document.readyState === 'complete') {
        //var grp_contract = document.getElementsByClassName('form-group field-contract')[0];
        var sel_with_contract = document.getElementById('id_with_contract');
        var sel2_with_contract = document.querySelector('[aria-controls="select2-id_with_contract-container"]');
        
        toggleContract(sel_with_contract.options[sel_with_contract.selectedIndex].text === 'Yes');

        var observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'attributes' && mutation.attributeName === 'aria-activedescendant') {
                    toggleContract(mutation.target.textContent === 'Yes');
                }
            });
        });
        
        observer.observe(sel2_with_contract, {
            attributes: true, // listen to attribute changes
            attributeFilter: ['aria-activedescendant'],
        });
    }
}