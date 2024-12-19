<?php
    $filename = "real-input.txt";
    $myfile = fopen($filename, "r"); 

    if($myfile){
        $content = fread($myfile,filesize($filename));
        fclose($myfile);
        $lines = explode("\n",$content);
        $res = 0;

        foreach($lines as $report){
            if(strlen($report) === 0) continue;

            $inc = false;
            $isvalid  = true;
            $levels = explode(" ",$report);
            
            for ($i = 0; $i < count($levels)-1; $i++) {
                $current = $levels[$i];
                $next = $levels[$i+1];

                if($i === 0){
                    $inc = $current < $next;
                }

                $diff;

                if($inc){
                    $diff = $next - $current;
                }else {
                    $diff = $current - $next;
                }

                if($diff < 1 || $diff > 3) {
                    $isvalid = false;
                    break;
                }
            }

            if($isvalid) {
                $res+=1;
                echo "Safe: $report\n";
            }else {
                echo "Unsafe: $report\n";
            }

        };

        echo "Result: $res";
    }else {
        echo "Failed to open the file.";
    }
?>
