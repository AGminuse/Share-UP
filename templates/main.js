function ChangeToDir(dir) {
  document.getElementById("el").remove();
  const xhr = new XMLHttpRequest();
  xhr.open("GET", `ChangeToDir${dir}`);
  xhr.send();
  xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      document.getElementById("demo").innerHTML = xhr.response.slice(1, -1);
      document.getElementById("path").setAttribute("value", dir);
      var myTextfield = document.getElementById("path");
      myTextfield.scrollIntoView({ behavior: "instant", inline: "nearest" });
    } else {
      console.log(`Error: ${xhr.status}`);
    }
  };
}
function GetFile(file) {
  window.location.href = `GetFile${file}`;
}
function go(dir) {
  ChangeToDir(document.getElementById("path").value);
}
