return
{
    on =
    {
        -- devices 1827 and 1828 are the HW Batteries Active Power devices, replace then with your device ids
        devices = {1827, 1828}
    },
	execute = function(domoticz, item)
        local battery1Power = domoticz.devices(1827)    -- Battery set 1, existing Active Power device
        local battery2Power = domoticz.devices(1828)    -- Battery set 2, existing Active Power device
        -- Create manually a dummy kWh, Electricity (instant and counter) device in generation mode
        local totalPower = domoticz.devices(1813)       -- Total, to be used in Energy dashboard configuration
        
        totalPower.updateElectricity(
        	battery1Power.actualWatt + battery2Power.actualWatt,
        	battery1Power.WhTotal + battery2Power.WhTotal)
	end
}
