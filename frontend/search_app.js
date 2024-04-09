let allLogs = [];
let currentPage = 1;
const pageSize = 50;

let startIndex, endIndex;
let data_fetched = false;

function fetchLogs() {
  const logs = getLogsForCurrentPage();
  displayLogs(logs);
  prevButton.style.visibility = currentPage > 1 ? "visible" : "hidden";
  nextButton.style.visibility = endIndex < allLogs.length ? "visible" : "hidden";
}

function getLogsForCurrentPage() {
  startIndex = (currentPage - 1) * pageSize;
  endIndex = startIndex + pageSize;
  return allLogs.slice(startIndex, endIndex);
}

function displayLogs(logs) {
  const logsTable = document.getElementById("logsTable");
  const logsBody = document.getElementById("logsBody");
  logsBody.innerHTML = "";

  logs.forEach((log) => {
    const row = logsBody.insertRow();
    const cellLevel = row.insertCell(0);
    const cellMessage = row.insertCell(1);
    const cellTimestamp = row.insertCell(2);
    const cellResourceId = row.insertCell(3);
    const cellTraceId = row.insertCell(4);
    const cellSpanId = row.insertCell(5);
    const cellCommit = row.insertCell(6);
    const cellParentResourceId = row.insertCell(7);

    cellLevel.innerHTML = log.level;
    cellMessage.innerHTML = log.message;
    cellTimestamp.innerHTML = log.timestamp;
    cellResourceId.innerHTML = log.resourceId;
    cellTraceId.innerHTML = log.traceId;
    cellSpanId.innerHTML = log.spanId;
    cellCommit.innerHTML = log.commit;
    cellParentResourceId.innerHTML = log.parentResourceId;
  });
  //   console.log("Table display:", logsTable.style.display);
}

function nextPage() {
    this.disabled = true;
  if (currentPage * pageSize < allLogs.length) {
    currentPage++;
      fetchLogs();
    }
    this.disabled = false;
}

function previousPage() {
  if (currentPage > 1) {
    currentPage--;
      fetchLogs();
    }
}

// Add event listeners for the buttons
document.getElementById("prevButton").addEventListener("click", updatePageCounter);
document.getElementById("nextButton").addEventListener("click", updatePageCounter);

function getLogs() {
  const level = document.getElementById("level").value;
  const message = document.getElementById("message").value;
  const resourceId = document.getElementById("resourceId").value;
  const timestamp = document.getElementById("timestamp").value;
  const traceId = document.getElementById("traceId").value;
  const spanId = document.getElementById("spanId").value;
  const commit = document.getElementById("commit").value;
  const parentResourceId = document.getElementById("parentResourceId").value;
  const startTimestamp = document.getElementById("startTimestamp").value;
  const endTimestamp = document.getElementById("endTimestamp").value;

  let url = `http://127.0.0.1:3000/logs?`;
  if (level) url += `level=${level}&`;
  if (message) url += `message=${message}&`;
  if (resourceId) url += `resourceId=${resourceId}&`;
  if (timestamp) url += `timestamp=${timestamp}&`;
  if (traceId) url += `traceId=${traceId}&`;
  if (spanId) url += `spanId=${spanId}&`;
  if (commit) url += `commit=${commit}&`;
  if (parentResourceId) url += `parentResourceId=${parentResourceId}&`;
  if (startTimestamp) url += `startTimestamp=${startTimestamp}&`;
  if (endTimestamp) url += `endTimestamp=${endTimestamp}&`;

  return fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // Log received data
      // Check if 'logs' property exists in the data object
      if (data && Array.isArray(data)) {
        allLogs = data;
        currentPage = 1;
        fetchLogs();
        if(data_fetched == false)
          showButtons();
        dataFetched = true;
        updatePageCounter();
      } else {
        console.error("Invalid data format:", data);
      }
    })
    .catch((error) => console.error("Error:", error));
}

function showButtons() {
  // Get references to the next and previous buttons
  const nextButton = document.getElementById("nextButton");
  const prevButton = document.getElementById("prevButton");

  // Make the buttons visible
  nextButton.style.display = "inline-block";
prevButton.style.display = "inline-block";
document
  .getElementById("prevButton")
  .addEventListener("click", previousPage, { once: true });
document
  .getElementById("nextButton")
  .addEventListener("click", nextPage, { once: true });
}

function updatePageCounter() {
// console.log(currentPage);
  totalPages = Math.ceil(allLogs.length / pageSize);
  // Update the page counter text
  const pageCounter = document.getElementById("pageCounter");
  pageCounter.textContent = `Page ${currentPage} of ${totalPages}`;
}

// Initial fetch on page load (replace with your actual API call)
// allLogs = getLogs();
// fetchLogs();
