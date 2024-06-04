document.addEventListener('DOMContentLoaded', function() {
    const regexInputField = document.getElementById('regex-input');
    const flagsInputField = document.getElementById('flags-input');
    const textInputField = document.getElementById('text-input');

    const onInputChange = () => {
        highlightMatches(regexInputField, flagsInputField, textInputField);
    };

    // Event listeners for input field changes
    regexInputField.addEventListener('input', onInputChange);
    flagsInputField.addEventListener('input', onInputChange);
    textInputField.addEventListener('input', onInputChange);

    const flagsInfoBtn = document.getElementById('flags-info-btn');
    const flagsInfoDropdown = document.getElementById('flags-info-dropdown');

    // Click event for the flags info button
    flagsInfoBtn.addEventListener('click', function(event) {
        flagsInfoDropdown.style.display = flagsInfoDropdown.style.display === 'none' ? 'block' : 'none';
        event.stopPropagation(); // Prevent event from propagating to the document
    });

    // Close the dropdown if clicked outside
    document.addEventListener('click', function() {
        if (flagsInfoDropdown.style.display === 'block') {
            flagsInfoDropdown.style.display = 'none';
        }
    });

    // Initial call to show highlights if any on page load with pre-filled values
    highlightMatches(regexInputField, flagsInputField, textInputField);
});

// highlight matches in the text input field
function highlightMatches(regexInputField, flagsInputField, textInputField) {
    const regexInput = regexInputField.value;
    const flagsInput = flagsInputField.value;
    const textInput = textInputField.value;
    const output = document.getElementById('output');

    output.innerHTML = '';
    regexInputField.style.backgroundColor = '';
    flagsInputField.style.backgroundColor = '';
    output.className = '';

    try {
        const regex = new RegExp(regexInput, flagsInput);
        let match;
        let lastIndex = 0;
        let isLightBlue = true;
        let matchesFound = false;

        if (flagsInput.includes('g')) {
            while ((match = regex.exec(textInput)) !== null) {
                matchesFound = true;
                output.appendChild(document.createTextNode(textInput.slice(lastIndex, match.index)));

                const span = document.createElement('span');
                span.className = isLightBlue ? 'highlight-blue' : 'highlight-darkblue';
                span.textContent = match[0];
                output.appendChild(span);

                isLightBlue = !isLightBlue;
                lastIndex = regex.lastIndex;

                if (match[0].length === 0) {
                    regex.lastIndex++;
                }
            }
        } else {
            match = regex.exec(textInput);
            if (match) {
                matchesFound = true;
                output.appendChild(document.createTextNode(textInput.slice(0, match.index)));

                const span = document.createElement('span');
                span.className = 'highlight-blue';
                span.textContent = match[0];
                output.appendChild(span);

                lastIndex = match.index + match[0].length;
            }
        }

        if (!matchesFound) {
            output.textContent = "No matches found.";
        } else if (lastIndex < textInput.length) {
            output.appendChild(document.createTextNode(textInput.slice(lastIndex)));
        }
    // throw error message
    } catch (e) {
        output.textContent = e.message;
        output.className = 'highlight-darkblue';
        regexInputField.style.backgroundColor = 'lightcoral';
        flagsInputField.style.backgroundColor = 'lightcoral';
    }
}
