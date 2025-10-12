Attribute VB_Name = "WeeklyUpdatesImport"
Option Explicit

' Usage:
' 1) Open Hybrid_ProjectPlan_Template.xlsx
' 2) Press ALT+F11, go to File > Import File..., and select this .bas file
' 3) In Excel, add a button (Developer tab) and assign the macro ImportWeeklyUpdates
' 4) Run the macro, select your CSV file with columns:
'    Week Start, Tickets Opened, Tickets Resolved, NPS, CSAT, Notes

Public Sub ImportWeeklyUpdates()
    Dim ws As Worksheet
    Dim filePath As Variant
    Dim fNum As Integer
    Dim line As String
    Dim parts() As String
    Dim nextRow As Long
    
    Set ws = ThisWorkbook.Sheets("Weekly_Updates")
    filePath = Application.GetOpenFilename("CSV Files (*.csv),*.csv", , "Select Weekly Updates CSV")
    If filePath = False Then Exit Sub
    
    fNum = FreeFile
    Open filePath For Input As #fNum
    
    ' Find next empty row
    nextRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row + 1
    If nextRow < 4 Then nextRow = 4
    
    Do While Not EOF(fNum)
        Line Input #fNum, line
        If Len(Trim(line)) > 0 Then
            parts = Split(line, ",")
            ' Expecting 6 columns
            If UBound(parts) >= 5 Then
                ws.Cells(nextRow, 1).Value = parts(0) ' Week Start
                ws.Cells(nextRow, 2).Value = parts(1) ' Tickets Opened
                ws.Cells(nextRow, 3).Value = parts(2) ' Tickets Resolved
                ws.Cells(nextRow, 4).Value = parts(3) ' NPS
                ws.Cells(nextRow, 5).Value = parts(4) ' CSAT
                ws.Cells(nextRow, 6).Value = parts(5) ' Notes
                nextRow = nextRow + 1
            End If
        End If
    Loop
    
    Close #fNum
    MsgBox "Weekly updates imported. Refresh KPI Dashboard if needed.", vbInformation
End Sub