from bottle import route, run, template, request
from pyfiglet import FigletFont, Figlet


@route('/')
def index():
    return template(
        '''
            <p></p>
            <form action="doform">
            <label for="string">Text:</label>
            <input type="text" id="string" name="text" value="TEST TEXT">
            <select name="font">
            <option disabled>Select font</option>
        '''
        + ''.join(f'''<option value = "{font}">{font}</option>\n''' for font in sorted(FigletFont.getFonts())) +
        '''
            </select>
            <label for="color">Color:</label>
            <input type="color" name="color">
            <button type="submit">Submit</button>
            </form>
            <p></p>
        '''
    )


@route('/doform')
def doform():
    color = request.query.color
    text = Figlet(request.query.font).renderText(request.query.text)
    return template(
        ''.join(f'''<p></p><pre style="color: {color};">''')
        + ''.join(f'''{text}</pre><p></p>''')
    )


run(host='localhost', port=8080, debug=True)
