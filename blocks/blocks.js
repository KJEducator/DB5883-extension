Blockly.defineBlocksWithJsonArray([
{
  "type": "hmc5883_compass_heading",
  "message0": "HMC5883 compass heading (°)",
  "output": null,
  "colour": "#0f3058",
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "hmc5883_magnetic_force",
  "message0": "HMC5883 magnetic force (uT) %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "axis",
      "options": [
        [
          "x",
          "0"
        ],
        [
          "y",
          "1"
        ],
        [
          "z",
          "2"
        ],
        [
          "strength",
          "3"
        ]
      ]
    }
  ],
  "output": null,
  "colour": "#0f3058",
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "hmc5883_calibrate_compass",
  "message0": "HMC5883 calibrate",
  "previousStatement": null,
  "nextStatement": null,
  "colour": "#0f3058",
  "tooltip": "",
  "helpUrl": ""
}
]);
