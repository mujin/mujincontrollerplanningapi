# -*- coding: utf-8 -*-
# Copyright (C) 2016 MUJIN Inc
__author__ = 'Denys Kanunikov'

from . import _

#
# Properties has to be in alphabetic order by name!!!
#

postCycleExecutionConfigSchema = {
    "title": _("Post cycle execution configurations"),
    "description": _("Post cycle execution and conveyor parameters."),
    "type": "object",
    "properties": {
        "circularMeasuringDistanceSpeed":{
            "title": _("Circular Measuring Speed"),
            "description": _("The maximum allowed speed for measuring trajectory"),
            "type": "number",
            "minimum": 0,
            "tags":["advanced", "motion", "si", "distsensor"]
        },
        "compartmentLength":{
            "title": _("Compartment Length"),
            "description": _("Length of the conveyor's placement compartment (mm)"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "conveyorLength":{
            "title": _("Conveyor Length"),
            "description": _("Length of the conveyor (mm)"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "conveyorSpeed": {
            "title" : _("Conveyor Speed"),
            "description" : _("Speed of the conveyor (mm/s)"),
            "type": "number",
            "minimum": 0.0,
            "default": 1000,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "distSensorMaxDist": {
            "title": _("Distance Sensor Max Distance"),
            "description": _("Maximum distance from the sensor to the object (mm)"),
            "type": "number",
            "minimum": 0.0,
            "tags":["advanced", "distsensor", "system", "si"]
        },
        "distSensorMinDist": {
            "title": _("Distance Sensor Min Distance"),
            "description": _("Minimum allowed distance from the sensor to the object in mm"),
            "type": "number",
            "minimum": 0.0,
            "tags":["advanced", "distsensor", "system", "si"]
        },
        "distSensorName": {
            "title": _("Distance Sensor Name"),
            "description": _("Name of the distance sensor body in environment"),
            "type": "string",
            "tags":["advanced", "distsensor", "si", "system"]
        },
        "distSensorToPlaceOffset": {
            "title": _("Sensor To Place Offset"),
            "description" : _("Offset from the sensor to the placement position by Z axis (mm)"),
            "type" : "number",
            "tags":["deprecated", "si", "motion", "system", "distsensor"]
        },
        "distSensorUri": {
            "title": _("Distance Sensor URI"),
            "description": _("COM 2 port: URI = serial:///dev/ttyS1?baud=9600&bytesize=8&parity=N&stopbits=1&timeout=0.02&offset=600&type=keyenceIL1000"),
            "type": "string",
            "tags":["advanced", "distsensor", "si", "system"],
            "format": "uri"
        },
        "encoderRatio":{
            "title": _("Encoder Ratio Pulse/mm"),
            "description": _("Ratio of encoder pulses to mm, how much pulses equivalent to 1 mm of conveyor belt"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "encoderReadDelay":{
            "title": _("Encoder Read Delay"),
            "description": _("Delay of the reading value from the conveyor encoder in seconds"),
            "type": "number",
            "minimum": 0.0,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "fLineSensorOffset":{
            "title": _("Line Sensor Position"),
            "description": _("The position of the placement sensor from the beginning of the conveyor belt from the encoder sensor (mm)"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "system", "conveyor"]
        },
        "grabbingaccelmult":{
            "title": _("Grabbing Accel Mult"),
            "description": _("How much to constraint the max accelerations so that parts do not fly out of hand. 1.0 means no constraint, smaller value makes movements slower"),
            "type": "number",
            "minimum": 0.01,
            "maximum": 1.0,
            "tags":["advanced", "si", "transfer", "motion"]
        },
        "ignorePlacementBodyNames":{
            "title": _("Ignore placement bodies names"),
            "description": _("bodies specified in the list will be ignored for collision checking while placing on the conveyor belt"),
            "type": "array",
            "items": {"type":"string"},
            "tags":["advanced", "si", "conveyor", "motion"],
        },
        "maxPlaceZDeceleration":{
            "title": _("Max Place Z Deceleration"),
            "description": _("The deceleration (mm/s) by Z axis with which robot can decelarate by Z axis during the placement of the item on the conveyor. If it's big, the part could fall out of the hand"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "motion", "target"]
        },
        "measuringDistancsRadius":{
            "title": _("Circular Measuring Radius"),
            "description": _("Radius of the circle (mm) which the manipulator uses for measuring trajectory"),
            "type": "number",
            "minimum": 0,
            "tags":["advanced", "si", "distsensor", "motion"]
        },
        "minBoxCheckThreshold":{
            "title": _("Min Box Check Threshold"),
            "description": _("If the box has width/depth less than these dimensions (mm), then robot will circle around the sensor in order to make sure it scanned the bottom."),
            "type": "number",
            "minimum": 0,
            "tags":["advanced", "si", "system", "distsensor"]
        },
        "minTargetHeight": {
            "title":_("Min Target Height"),
            "description":_("If the sensor measures any target heights lower than this value (mm), will clamp it to this value"),
            "type":"number",
            "minimum":0.1,
            "tags":["advanced", "si", "system", "motion"]
        },
        "minTargetHeightForSensor": {
            "title": _("Min Target Height for Sensor"),
            "description": _("If target height is less than this value (mm), then will skip the sensor measurement and go directly to placing the part down"),
            "type": "number",
            "minimum": 0.1,
            "tags":["advanced", "si", "system", "distsensor"]
        },
        "placename":{
            "title": _("Placement Goal Name"),
            "description": _("Name of the IK parameter on the destination body"),
            "type": "string",
            "tags":["medium", "si", "system"]
        },
        "postCycleType": {
            "title": _("Post Cycle Type"),
            "description": _("Type of the post cycle execution."),
            "type": "string",
            "default": "",
            "enum": ["", "conveyorplace"], 
            "tags":["basic", "si", "system"]
        },
        "robotOffset":{
            "title": _("Robot Offset"),
            "description": _("The position of the robot from the beginning of the conveyor belt from the encoder sensor (mm)"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "system", "conveyor", "motion"]
        },
        # "encoderIndex":{ # moved to direct editing from robotControllerOptions
        #     "title": _("Index of the encoder for tracking 0 position of the conveyor belt"),
        #     "type": "integer",
        #     "minimum": 0
        # },
        "useDistSensor":{
            "title": _("Use Distance Sensor"),
            "description": _("If true, will use distance sensor measurements to get the box height."),
            "type": "boolean",
            "minimum": 0.0,
            "tags":["basic", "si", "system", "distsensor"]
        },
        "xacceloffset": {
            "title": _("X Accel Offset"),
            "description": _("The distance (mm) to travel in order to acceleration at conveyor speed along its movement"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "motion", "conveyor"]
        },
        "xoffset": {
            "title": _("X Offset"),
            "description": _("The distance (mm) to travel when going down to place to the conveyor"),
            "type": "number",
            "minimum": 0,
            "tags":["basic", "si", "motion", "conveyor"]
        },
        "zoffset": {
            "title": _("Max Target Height"),
            "description": _("The distance (mm) to start from the place point and go down, this has to be bigger or equal to the maximum height of the item on the conveyor"),
            "type": "number",
            "minimum": 0,
            "tags":["advanced", "si", "motion", "conveyor"]
        }
    }
}
