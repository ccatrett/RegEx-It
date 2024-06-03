document.getElementById('regex-input').addEventListener('input', highlightMatches);
document.getElementById('flags-input').addEventListener('input', highlightMatches);
document.getElementById('text-input').addEventListener('input', highlightMatches);

function highlightMatches() {
    const regexInputField = document.getElementById('regex-input');
    const flagsInputField = document.getElementById('flags-input');
    const regexInput = regexInputField.value;
    const flagsInput = flagsInputField.value;
    const textInput = document.getElementById('text-input').value;
    const output = document.getElementById('output');
    
    // Clear the previous output and reset input field colors
    output.innerHTML = '';
    regexInputField.style.backgroundColor = '';
    flagsInputField.style.backgroundColor = '';

    // Validate the regular expression and flags
    try {
        let regex;
        try {
            regex = new RegExp(regexInput, flagsInput);
        } catch (e) {
            throw new Error('Invalid regex pattern or flags');
        }

        // Find matches and highlight them
        let lastIndex = 0;
        let match;
        let isLightBlue = true;

        if (flagsInput.includes('g')) {
            while ((match = regex.exec(textInput)) !== null) {
                // Append text before the match
                output.appendChild(document.createTextNode(textInput.slice(lastIndex, match.index)));

                // Create a span for the match with alternating colors
                const span = document.createElement('span');
                span.className = isLightBlue ? 'highlight-blue' : 'highlight-darkblue';
                span.textContent = match[0];
                output.appendChild(span);

                // Toggle color
                isLightBlue = !isLightBlue;

                lastIndex = regex.lastIndex;

                // Prevent infinite loop for zero-length matches
                if (match.index === regex.lastIndex) {
                    regex.lastIndex++;
                }
            }
        } else {
            // Default to finding only the first match if no 'g' flag is set
            match = regex.exec(textInput);
            if (match) {
                output.appendChild(document.createTextNode(textInput.slice(0, match.index)));
                
                // Create a span for the match
                const span = document.createElement('span');
                span.className = 'highlight-blue';
                span.textContent = match[0];
                output.appendChild(span);

                output.appendChild(document.createTextNode(textInput.slice(match.index + match[0].length)));
            } else {
                output.appendChild(document.createTextNode(textInput));
            }
        }
    } catch (e) {
        // If there's an error in regex, clear the output and set input field color to light red
        regexInputField.style.backgroundColor = 'lightcoral';
        flagsInputField.style.backgroundColor = 'lightcoral';
        console.error(e.message);
    }
}

