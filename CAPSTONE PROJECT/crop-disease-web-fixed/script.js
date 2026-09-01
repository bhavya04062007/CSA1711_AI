const pages=["home","disease-info","detect","history","about"];
let selectedFile=null;
const demoHistory=[
 {crop:"Tomato",disease:"Early Blight",status:"Diseased",confidence:"94%",date:"Demo record"},
 {crop:"Apple",disease:"Apple Scab",status:"Diseased",confidence:"91%",date:"Demo record"},
 {crop:"Pepper",disease:"Healthy",status:"Healthy",confidence:"97%",date:"Demo record"}
];

function showPage(id){
  pages.forEach(p=>document.getElementById(p).classList.toggle("active",p===id));
  window.scrollTo({top:0,behavior:"smooth"});
  document.getElementById("navLinks").classList.remove("open");
  history.replaceState(null,"","#"+id);
}
function toggleMenu(){document.getElementById("navLinks").classList.toggle("open")}
function previewImage(event){
  const file=event.target.files[0];
  if(!file)return;
  if(!["image/jpeg","image/png"].includes(file.type)){alert("Please choose a JPG, JPEG or PNG image.");return}
  selectedFile=file;
  const reader=new FileReader();
  reader.onload=e=>{
    document.getElementById("preview").src=e.target.result;
    document.getElementById("previewWrap").classList.remove("hidden");
    document.getElementById("uploadBox").classList.add("hidden");
    document.getElementById("fileName").textContent=file.name;
    document.getElementById("analyzeBtn").disabled=false;
  };
  reader.readAsDataURL(file);
}
function removeImage(event){
  event.stopPropagation();
  selectedFile=null;
  document.getElementById("imageInput").value="";
  document.getElementById("previewWrap").classList.add("hidden");
  document.getElementById("uploadBox").classList.remove("hidden");
  document.getElementById("analyzeBtn").disabled=true;
  resetResult();
}
function resetResult(){
  document.getElementById("resultPanel").innerHTML='<div class="result-empty"><div class="big-icon">🌿</div><h3>Your result will appear here</h3><p>Upload an image and click Analyze Image.</p></div>';
}
function analyzeImage(){
  if(!selectedFile)return;
  const btn=document.getElementById("analyzeBtn");
  btn.disabled=true;
  btn.textContent="Analyzing...";
  document.getElementById("resultPanel").innerHTML='<div class="result-empty"><div class="big-icon">🤖</div><h3>Analyzing image...</h3><p>Please wait a moment.</p></div>';
  setTimeout(()=>{
    document.getElementById("resultPanel").innerHTML=`
      <div class="result-content">
        <span class="demo-badge">DEMO RESULT — NOT A REAL AI PREDICTION</span>
        <h3 class="result-title">Tomato Early Blight</h3>
        <div class="result-grid">
          <div class="result-item"><small>Crop</small><strong>Tomato</strong></div>
          <div class="result-item"><small>Status</small><strong class="status-danger">Diseased</strong></div>
          <div class="result-item"><small>Disease</small><strong>Early Blight</strong></div>
          <div class="result-item"><small>Confidence</small><strong>94% (demo)</strong></div>
        </div>
        <div class="confidence"><small>Demo confidence</small><div class="bar"><span></span></div></div>
        <div class="info-box"><h4>🩺 Disease Information</h4><p><strong>Symptoms:</strong> Brown spots and yellowing may appear on leaves.</p><p><strong>Prevention:</strong> Maintain plant spacing and avoid excessive moisture.</p><p><strong>Management:</strong> Monitor affected leaves and follow suitable crop-management practices.</p></div>
        <div class="info-box"><h4>Top Predictions — Demo Data</h4><p>1. Tomato Early Blight — 94%</p><p>2. Tomato Late Blight — 3%</p><p>3. Tomato Healthy — 3%</p></div>
        <button class="secondary-btn full" onclick="resetDetection()">↻ New Prediction</button>
      </div>`;
    btn.disabled=false;
    btn.textContent="Analyze Image";
  },900);
}
function resetDetection(){removeImage(new Event("click"))}
function renderHistory(items=demoHistory){
  const list=document.getElementById("historyList");
  if(!items.length){list.innerHTML='<div class="card" style="text-align:center">No matching demo records.</div>';return}
  list.innerHTML=items.map(x=>`<div class="history-card"><div><small>Crop</small><strong>${x.crop}</strong></div><div><small>Disease</small><strong>${x.disease}</strong></div><div><small>Status</small><strong class="${x.status==="Diseased"?"status-danger":""}">${x.status}</strong></div><div><small>Confidence</small><strong>${x.confidence}</strong><small>${x.date}</small></div></div>`).join("");
}
function filterHistory(){
  const q=document.getElementById("historySearch").value.toLowerCase();
  const f=document.getElementById("historyFilter").value;
  renderHistory(demoHistory.filter(x=>(f==="all"||x.status===f)&&(`${x.crop} ${x.disease}`).toLowerCase().includes(q)));
}
window.addEventListener("load",()=>{
  renderHistory();
  const id=location.hash.replace("#","");
  if(pages.includes(id))showPage(id);else showPage("home");
});
