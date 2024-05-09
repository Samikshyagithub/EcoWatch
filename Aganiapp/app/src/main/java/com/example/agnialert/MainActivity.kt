package com.example.agnialert

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.Button
import androidx.compose.material3.Checkbox
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarResult
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.agnialert.ui.theme.AgniAlertTheme
import com.google.android.gms.maps.model.CameraPosition
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.compose.GoogleMap
import com.google.maps.android.compose.MapProperties
import com.google.maps.android.compose.MapType
import com.google.maps.android.compose.Marker
import com.google.maps.android.compose.MarkerState
import com.google.maps.android.compose.rememberCameraPositionState
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            Scaffold(modifier = Modifier.fillMaxSize()) { padding ->
                Column(Modifier.padding(padding)) {
                    agniAlert()
                }
            }
        }
    }
}

@Composable
@Preview
fun agniAlert(){

    Column(modifier = Modifier.fillMaxSize(), horizontalAlignment = Alignment.CenterHorizontally) {
        Text(text = " Agani Alert", fontSize = 24.sp, fontWeight = FontWeight.Bold)

        Spacer(modifier = Modifier.size(10.dp, 20.dp))

        Row(modifier = Modifier
            .fillMaxHeight(0.5f)
            .fillMaxWidth()) {
            MapScreen()
        }

        Spacer(modifier = Modifier.size(10.dp, 20.dp))

        Row (modifier = Modifier.fillMaxSize()){
            reportAlert()
        }
    }

}

@Composable
fun MapScreen() {
    val kathmanduUniversity = LatLng(27.61930904485903, 85.53867363700307)

    val cameraPositionState = rememberCameraPositionState {
        position = CameraPosition.fromLatLngZoom(kathmanduUniversity, 18f)
    }

    var properties by remember {
        mutableStateOf(MapProperties(mapType = MapType.TERRAIN))
    }

    GoogleMap(
        modifier = Modifier.fillMaxSize(),
        cameraPositionState = cameraPositionState,
        properties = properties
    ) {
        Marker(
            state = MarkerState(position = kathmanduUniversity),
            title = "Report Alert"
        )
    }
}

@Composable
fun reportAlert(){

    var buttonText by remember { mutableStateOf("Submit Alert")}

    Column(modifier = Modifier.fillMaxSize(), horizontalAlignment = Alignment.CenterHorizontally) {

        Text(text = "Do you want to report alert?", fontSize = 18.sp, fontWeight = FontWeight.Bold)

        checkOptions()

        Button(onClick = {
            buttonText = "Your report is Submitted"
        }) {
            Text(text = buttonText)
        }


    }

}

@Composable
fun checkOptions(){
    val options = listOf("Police", "Ambulance", "Fire Brigade")
    val selectedOptions = remember {
        mutableStateListOf<String>()
    }

    Column {
        options.forEach { option ->
            Row {
                Checkbox(
                    checked = selectedOptions.contains(option),
                    onCheckedChange = { isChecked ->
                        if (isChecked) {
                            selectedOptions.add(option)
                        } else {
                            selectedOptions.remove(option)
                        }
                    },
                    modifier = Modifier.padding(0.dp)
                )
                Text(text = option, modifier = Modifier.padding(vertical = 9.dp))
        }

        }
    }
}