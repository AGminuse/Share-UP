const xhr = new XMLHttpRequest();
xhr.open("GET", "DIR");
xhr.send();
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    document.getElementById("demo").innerHTML = xhr.response;
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
const xhr2 = new XMLHttpRequest();
xhr2.open("GET", "ROOTDIR");
xhr2.send();
xhr2.onload = () => {
  if (xhr2.readyState == 4 && xhr2.status == 200) {
    document
      .getElementById("path")
      .setAttribute("value", xhr2.response.slice(1, -1));
    //document.getElementById("demo").innerHTML = xhr.response;
  } else {
    console.log(`Error: ${xhr2.status}`);
  }
};
