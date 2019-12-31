import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow{
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "My Window"

    Item {
        id: page
        visible: true
        width: parent.width

        Rectangle{
            id: myRectangle
            height: {
                /* Here we can add javascript code */
                return 160
            }
            width: parent.width

            color: "#ff0000"
            
            Text {
                id: mainText
                text: "I'm some regular text"
                height: 50
                width: parent.width
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter                
            }

            Button {
                id: mainButton
                text: "Push me"
                anchors.top: mainText.bottom
                onClicked: {
                    if (myRectangle.color == "#ff0000"){
                        myRectangle.color = "#008000"
                    } else {
                        myRectangle.color = "#ff0000"
                    }
                }
            }
        }
    }

}