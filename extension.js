({
    name: "DB5883", // Category Name
    description: "3-Axis Digital Compass",
    author: "K",
    category: "Sensors",
    version: "1.0.0",
    icon: "/static/icon.png", // Category icon
    color: "#0f3058", // Category color (recommend some blocks color)
    blocks: [ // Blocks in Category
        "hmc5883_magnetic_force",
        "hmc5883_compass_heading",
        "hmc5883_calibrate_compass"
    ]
});
