function setfilename(val)
{
  var fileName = val.substr(val.lastIndexOf("\\")+1, val.length);
  document.getElementById("uploadFile").value = fileName;
}