package batch;

import datamodel.GeometryProfile;
import datamodel.RelatedGeometries;
import datareader.AbstractReader;
import utilities.IDocumentation;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.stream.JsonToken;


import java.util.Map;
import java.util.HashMap;
import java.io.FileWriter;
import java.io.IOException;

public abstract class AbstractBatchAlgorithm implements IDocumentation {
    
    protected final int datasetDelimiter;

    protected long indexingTime;
    protected long verificationTime;

    protected final GeometryProfile[] sourceData;
    protected final RelatedGeometries relations;
    protected final AbstractReader targetReader;
    
    public AbstractBatchAlgorithm(int qPairs, AbstractReader sourceReader, AbstractReader targetReader) {
        sourceData = sourceReader.getGeometryProfiles();
        
        relations = new RelatedGeometries(qPairs);
        datasetDelimiter = sourceData.length;
        
        this.targetReader = targetReader;
    }

    public AbstractBatchAlgorithm(int qPairs, AbstractReader sourceReader, AbstractReader targetReader, String exportPath) {
        sourceData = sourceReader.getGeometryProfiles();

        relations = new RelatedGeometries(qPairs, exportPath);
        datasetDelimiter = sourceData.length;

        this.targetReader = targetReader;
    }
    
    public void applyProcessing() {
        long time1 = System.currentTimeMillis();
        filtering();
        long time2 = System.currentTimeMillis();
        verification();
        long time3 = System.currentTimeMillis();
        indexingTime = time2 - time1;
        verificationTime = time3 - time2;
    }
    
    protected abstract void filtering();

    public void printResults(String json_output) {
        printResults(); 
        getResultsText(json_output);
    }
        
    public void printResults() {
        System.out.println(getResultsText());
    }
    
    public long getIndexingTime() {
        return indexingTime;
    }
    
    public RelatedGeometries getResults() {
        return relations;
    }
    

    public void getResultsText(String json_output){
        Gson gson = new GsonBuilder().setPrettyPrinting()
        .serializeSpecialFloatingPointValues()
        .registerTypeAdapter(Double.class, new TypeAdapter<Double>() {
            @Override
            public void write(JsonWriter out, Double value) throws IOException {
                if (value.isInfinite() || value.isNaN()) {
                    out.value("Infinity"); // or out.nullValue()
                } else {
                    out.value(value);
                }
            }
            @Override
            public Double read(JsonReader in) throws IOException {
                if (in.peek() == JsonToken.STRING) {
                    String str = in.nextString();
                    if ("Infinity".equals(str)) {
                        return Double.POSITIVE_INFINITY;
                    }
                }
                return in.nextDouble();
            }
        }).create();
        Map<String, Object> data = new HashMap<>();
        data.put("source_geometries",sourceData.length);
        data.put("target_geometries",targetReader.getSize());
        data.put("indexing_time", indexingTime);
        data.put("verification_time", verificationTime);
        data.put("qualifying_pairs",relations.getQualifyingPairs());
        data.put("exceptions", relations.getExceptions());
        data.put("detected_links", relations.getDetectedLinks());
        data.put("interlinked_geometries", relations.getInterlinkedPairs());
        data.put("no_of_contains", relations.getNoOfContains());
        data.put("no_of_covered_by", relations.getNoOfCoveredBy());
        data.put("no_of_covers", relations.getNoOfCovers());
        data.put("no_of_crosses", relations.getNoOfCrosses());
        data.put("no_of_equals", relations.getNoOfEquals());
        data.put("no_of_intersects", relations.getNoOfIntersects());
        data.put("no_of_overlaps", relations.getNoOfOverlaps());
        data.put("no_of_touches", relations.getNoOfTouches());
        data.put("no_of_within", relations.getNoOfWithin());
        data.put("recall", relations.getRecall());
        data.put("precision", relations.getPrecision());
        data.put("progressive_geometry_recall", relations.getProgressiveGeometryRecall());
        data.put("verified_pairs", relations.getVerifiedPairs());
        data.put("qualifying_pairs", relations.getQualifyingPairs());
        
        try {
            // Specify the output file path
            FileWriter writer = new FileWriter(json_output);
            gson.toJson(data, writer);
            writer.close();
            
            System.out.println("JSON file successfully created at: " + json_output);
        }
        catch (IOException e) {
            e.printStackTrace();
        }

    }


    public String getResultsText() {
        StringBuilder sb = new StringBuilder();
        sb.append("Source geometries\t:\t").append(sourceData.length).append("\n");
        sb.append("Target geometries\t:\t").append(targetReader.getSize()).append("\n");
        sb.append("Indexing time\t:\t").append(indexingTime).append("\n");
        sb.append("Verification time\t:\t").append(verificationTime).append("\n");
        sb.append(relations.print()).append("\n");
        return sb.toString();
    }
    
    public int getSourceGeometries() {
        return sourceData.length;
    }
    
    public int getTargetGeometries() {
        return targetReader.getSize();
    }
    
    public long getVerificationTime() {
        return verificationTime;
    }
    
    protected abstract void verification();
}
