package jsonWorkflow;
import datareader.AbstractReader;
import enums.BatchAlgorithms;
import enums.DataType;
import enums.ProgressiveAlgorithms;

import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

import com.google.gson.*;
import com.google.gson.stream.JsonReader;
import com.opencsv.bean.opencsvUtils;

import static workflowManager.CommandLineInterfaceUtils.*;




public class JsonWorkflow {
    public static void main(String[] args) {
        System.out.println("Welcome to JedAI-spatial JsonWorkflow");
        System.out.println("Reading " + args[0]);

        try (FileReader reader = new FileReader(args[0])){
            JsonReader j_reader = new JsonReader(reader);
            JsonParser j_parser = new JsonParser();
            JsonElement json_element =  j_parser.parse(j_reader);
            JsonObject json_input = json_element.getAsJsonObject();

            System.out.println(json_input);
            


            // Source JSON 
            JsonObject source = json_input.get("source").getAsJsonObject();
            String sourceFilePath = source.get("path").getAsString();
            String sourceDataType_string = source.get("data_type").getAsString();
            System.out.println(DATA_TYPE[0].equals(sourceDataType_string));

            int sourceDataType = getIndex(sourceDataType_string, DATA_TYPE);
            System.out.println(sourceDataType);
            AbstractReader sourceReader = DataType.getReader(DataType.values()[sourceDataType], sourceFilePath, source);

            // Target JSON
            JsonObject target = json_input.get("target").getAsJsonObject();
            String targetFilePath = target.get("path").getAsString();
            String targetDataType_string = target.get("data_type").getAsString();
            int targetDataType = getIndex(targetDataType_string, DATA_TYPE);
            AbstractReader targetReader = DataType.getReader(DataType.values()[targetDataType], targetFilePath, target);
            String outputFile = null;
            if (json_input.has("output_path")) outputFile = json_input.get("output_path").getAsString();
            
            int algorithm = getIndex(json_input.get("algorithm").getAsString(), BATCH_ALGORITHMS);
            
            if (json_input.has("output_path") && args.length > 1) 
                BatchAlgorithms.runAlgorithm(BatchAlgorithms.values()[algorithm], sourceReader, targetReader, outputFile, args[1]);
            else if(json_input.has("output_path"))
                BatchAlgorithms.runAlgorithm(BatchAlgorithms.values()[algorithm], sourceReader, targetReader, outputFile);
            else 
                BatchAlgorithms.runAlgorithm(BatchAlgorithms.values()[algorithm], sourceReader, targetReader);

            


        }    
        catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
        catch (IllegalStateException e) {
            e.printStackTrace();
        }
        
    }        
    
}
