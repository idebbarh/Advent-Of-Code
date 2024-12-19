<?php
    $filename = "real-input.txt";
    $myfile = fopen($filename, "r"); 

function is_report_save($levels,$sublevels){
        $inc = false;
        $isvalid  = true;

        for ($i = 0; $i < count($sublevels)-1; $i++) {
            $current = $sublevels[$i];
            $next = $sublevels[$i+1];

            if($i === 0){
                $inc = $current < $next;
            }

            $diff = 0;

            if($inc){
                $diff = $next - $current;
            }else {
                $diff = $current - $next;
            }


            if($diff < 1 || $diff > 3) {
                $sub1= array_merge(array_slice($levels, 0, $i), array_slice($levels, $i + 1));
                $sub2= array_merge(array_slice($levels, 0, $i+1), array_slice($levels, $i + 2));
                $sub3  = array_slice($levels, 1);
                $isvalid = false;

                if((count($levels) === count($sublevels))){
                    $res1 = is_report_save($levels,$sub1);
                    $res2 = is_report_save($levels,$sub2);
                    $res3 =is_report_save($levels,$sub3);

                    $isvalid =  $res1 || $res2 || $res3;
                }

                break;
            }
        }

        return $isvalid;
}

    if($myfile){
        $content = fread($myfile,filesize($filename));
        fclose($myfile);
        $lines = explode("\n",$content);
        $res = 0;

        foreach($lines as $report){
            if(strlen($report) === 0) continue;

            if(is_report_save(explode(" ",$report),explode(" ",$report))){
                $res+=1;
            }            


        };

        echo "Result: $res";
    }else {
        echo "Failed to open the file.";
    }
?>
