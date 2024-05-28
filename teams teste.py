import pymsteams

# Substitua <Microsoft Webhook URL> pela URL do seu webhook
myTeamsMessage = pymsteams.connectorcard("https://teams.microsoft.com/l/team/19%3AZf22uHWYzaZY6t6_L4U8Nduj3RPD0ThI0jTe-3t_RZM1%40thread.tacv2/conversations?groupId=7534ad9b-88d1-4e40-aaaa-60e30f98a9e7&tenantId=19cd0ad7-451d-4f5a-b33f-29b03f7a498a")
myTeamsMessage.text("teste")
myTeamsMessage.send()