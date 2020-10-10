Blockly.Python['hmc5883_compass_heading'] = function (block) {
  Blockly.Python.definitions_['import_HMC5883'] = 'import HMC5883';

  var code = 'int(HMC5883.heading())';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['hmc5883_magnetic_force'] = function (block) {
  Blockly.Python.definitions_['import_HMC5883'] = 'import HMC5883';

  var dropdown_axis = block.getFieldValue('axis');

  var code = `int(HMC5883.raw()[${dropdown_axis}])`;
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['hmc5883_calibrate_compass'] = function (block) {
  Blockly.Python.definitions_['import_HMC5883'] = 'import HMC5883';

  var code = 'HMC5883.calibrate()\n';
  return code;
};