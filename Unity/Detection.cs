using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Detection : MonoBehaviour
{
    public Transform player;
    public GameObject alerts;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {   
    
        if(player.rotation.z < -0.25){
            alerts.SetActive(true);
        }
        else{
            alerts.SetActive(false);
        }
        
    }
}
