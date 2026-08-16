async function detectFire() {
    const result = document.getElementById("result");

    result.innerHTML = "🔍 Detecting fire...";

    try {
        const response = await fetch("/detect", {
            method: "POST"
        });

        const data = await response.json();

        result.innerHTML =
            "🔥 <b>" + data.result + "</b><br>" +
            "Fire area detected: " + data.fire_area;

    } catch (error) {
        result.innerHTML = "❌ Error connecting to server";
    }
}