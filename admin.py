from flask import Flask,render_template,request, abort, jsonify, send_from_directory
import pandas as pd
import xlrd
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/download", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        '''print(request.files['file'])'''
        file_name = request.files['file']
        df = pd.read_excel(file_name)  # Read Excel file as a DataFrame
        df1 = pd.read_excel(file_name)  # Read Excel file as a DataFrame

        # assigning  shikeisho start status# dataframe to shikeisho start status#
        df['shikeisho start status#'] = df['shikeisho start status']
        df['shikeisho end status#'] = df['shikeisho end status']
        # shikeisho start status# replacing with oredefined status numbers.
        df['shikeisho start status#'] = df['shikeisho start status#'].replace(
            {'RD': '1', 'LM': '2', 'BOM': '3', 'PROC': '4', 'P_O': '5', 'SM': '6', 'PJA': '7'})
        df['shikeisho end status#'] = df['shikeisho end status#'].replace(
            {'RD': '1', 'LM': '2', 'BOM': '3', 'PROC': '4', 'P_O': '5', 'SM': '6', 'PJA': '7'})
        df['path'] = df['shikeishoNo'] + "." + df['shikeisho start status'] + "." + df['shikeisho end status'] + "." + \
                     df['shikeisho start status#'] + "." + df['shikeisho end status#']
        df['path_order'] = '1'

        df1['shikeisho start status#'] = df1['shikeisho start status']
        df1['shikeisho end status#'] = df1['shikeisho end status']
        df1['shikeisho start status#'] = df1['shikeisho start status#'].replace(
            {'RD': '1', 'LM': '2', 'BOM': '3', 'PROC': '4', 'P_O': '5', 'SM': '6', 'PJA': '7'})
        df1['shikeisho end status#'] = df1['shikeisho end status#'].replace(
            {'RD': '1', 'LM': '2', 'BOM': '3', 'PROC': '4', 'P_O': '5', 'SM': '6', 'PJA': '7'})
        df1['path'] = df['shikeishoNo'] + "." + df1['shikeisho start status'] + "." + df1[
            'shikeisho end status'] + "." + df1['shikeisho start status#'] + "." + df1['shikeisho end status#']
        df1['path_order'] = '2'

        dataf = pd.concat([df, df1])

        dataf1 = dataf.sort_values(by=['path', 'path_order'], ascending=True)

        dataf1.to_excel("final.xlsx")
    return render_template("download.html")
'''
@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
        return jsonify(files)

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)'''

if __name__ == "__main__":
    app.run(debug=True, port=9999)
