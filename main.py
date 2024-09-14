import uvicorn
import os
import tarfile
from pathlib import Path
from fastapi import FastAPI, Request,Response, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import PlainTextResponse,FileResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="static")


root_dir=Path(os.getcwd())

def update_list(rootdir:Path):
    dirs=[]
    files=[]
    html=""
    for d in rootdir.iterdir() :
        if d.is_dir():
            dirs.append(d)

        if d.is_file():
            files.append(d)
    #making Directorys
    for item in list(dirs) :
        html+="<li id='el' class='dir'> <a class='dir_button' onclick='ChangeToDir("
        html+='`'+item.__str__()+'`'+")'>"+"<img id='dir_img'>"
        html+=item.name
        html+="<img id='dir_compress'></a></li>"

    for item in files :
        html+="<li id='el' class='file'><a class='file_button' onclick='GetFile("
        html+='`'+item.__str__()+'`'+")'>"+"<img id='file_img'>"
        html+=item.name
        html+="</a></li>"
    return html



@app.get("/")
async def read_item(request: Request ):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
@app.get("/ROOTDIR")
async def send_rootDir():
    return root_dir.__str__()


@app.get("/DIR",response_class=PlainTextResponse)
async def send_directory():
    return update_list(Path(os.getcwd()))

@app.get("/ChangeToDir/{dir:path}")
async def changedir(dir):
    root_dir=Path("/"+dir)
    return update_list(root_dir)


@app.get("/GetFile/{file_name:path}",response_class=FileResponse)
def getfile(file_name):
    file_name="/"+file_name
    return FileResponse(file_name,filename=file_name.split("/")[-1])

@app.post("/UploadFile/",response_class=PlainTextResponse)
def uploadfile(files: list[UploadFile]):
        for file in files:
            f=open(file.filename.__str__(),mode="ab")
            f.flush()
            f.write(file.file.read())
        return "done"
uvicorn.run(app,host="0.0.0.0")
