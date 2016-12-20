import QtQuick 2.4
import QtQuick.Window 2.2
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.1

Window {
    visible: true
    minimumHeight: 480
    minimumWidth: 320

    Rectangle {
        id: rectangle1
        width: lo_column.implicitWidth
        height: lo_column.implicitHeight
        anchors.rightMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0
        anchors.fill: parent
        gradient: Gradient {
            GradientStop {
                position: 1
                color: "#ffffff"
            }

            GradientStop {
                position: 0.034
                color: "#1754cd"
            }
        }
        ColumnLayout {
            id: lo_column
            x: 0
            y: 0
            width: parent.width
            height: 640

            Text {
                id: txt_title
                //x: 187
                //y: 127
                width: 144
                height: 20
                color: "#f0efef"
                text: qsTr("Jabber ")
                horizontalAlignment: Text.AlignVCenter
                font.family: "Arial"
                font.bold: false
                font.pixelSize: 31

                Layout.alignment: Qt.AlignHCenter | Qt.AlignBottom
            }

            TextField {
                id: tf_username
                placeholderText: qsTr("Username")
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignBottom
                Layout.minimumHeight: 25
            }

            TextField {
                id: tf_password
                echoMode: 2
                placeholderText: qsTr("Password")
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.topMargin: 5
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignTop
                Layout.minimumHeight: 25
            }

            Text {
                id: txt_forgotpw
                x: 89
                y: 325
                width: 93
                height: 19
                color: "#ffffff"
                text: qsTr("Forgot password?")
                font.underline: true
                font.pixelSize: 11
                Layout.alignment: Qt.AlignTop | Qt.AlignLeft
                Layout.leftMargin : 20
                anchors.top: tf_password.bottom
                anchors.topMargin: 5

            }

            CheckBox {
                id: cb_autosignin
                x: 89
                y: 359
                text: qsTr("Sign me in when Jabber Starts")
                Layout.leftMargin: 20
                anchors.top: txt_forgotpw.bottom
                anchors.topMargin: 5


            }

            Button {
                id: btn_signin
                text: qsTr("Sign In")
                activeFocusOnPress: true
                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.fillWidth: true
                anchors.top: cb_autosignin.bottom
                anchors.topMargin: 5
                Layout.minimumHeight: 30
            }


        }
    }


}


