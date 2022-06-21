weapon_trigger = {
    "weapon_357",
    "weapon_crowbar",
    "gmod_tool"
}

hook.Add( "PlayerSwitchWeapon", "WeaponSwitchExample", function( ply, oldWeapon, newWeapon )
    for k, v in pairs(weapon_trigger) do
        if newWeapon:GetClass() == v then
            RunConsoleCommand("say", "/me sort un.e " .. newWeapon:GetClass())
        end
    end
    
end )